import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D

class DuopolyGame:
    
    def __init__(self):
        self.firm1_name = ""
        self.firm2_name = ""
        self.marginal_cost1 = 0
        self.marginal_cost2 = 0
        self.market_size = 0
        self.price_intercept = 0
        self.price_slope = 0
        
    def display_introduction(self):
        print("=" * 80)
        print(" " * 20 + "DUOPOLY GAME THEORY SIMULATOR")
        print("=" * 80)
        print("\n WHAT IS A DUOPOLY?")
        print("-" * 80)
        print("A duopoly is a market structure with only TWO firms selling similar products.")
        print("Key characteristics:")
        print("  1. Only two sellers control the entire market")
        print("  2. Firms are interdependent - each firm's profit depends on both actions")
        print("  3. Strategic behavior - firms must anticipate rival's reactions")
        print("\n REAL-WORLD EXAMPLES:")
        print("-" * 80)
        print("  • Coca-Cola vs Pepsi (Soft drinks)")
        print("  • Boeing vs Airbus (Commercial aircraft)")
        print("  • Visa vs Mastercard (Payment processing)")
        print("  • AMD vs Intel (Computer processors)")
        print("\n TWO MAIN MODELS:")
        print("-" * 80)
        print("  1. COURNOT MODEL: Firms compete on QUANTITY produced")
        print("  2. BERTRAND MODEL: Firms compete on PRICE set")
        print("=" * 80)
        input("\nPress Enter to continue...")
        
    def get_user_inputs(self):
        """Get user inputs for the duopoly simulation"""
        print("\n" + "=" * 80)
        print(" " * 25 + "SIMULATION SETUP")
        print("=" * 80)
        
        # Firm names
        self.firm1_name = input("\n Enter name of Firm 1 (e.g., Coca-Cola): ").strip()
        if not self.firm1_name:
            self.firm1_name = "Firm A"
            
        self.firm2_name = input(f" Enter name of Firm 2 (e.g., Pepsi): ").strip()
        if not self.firm2_name:
            self.firm2_name = "Firm B"
        
        # Marginal costs
        print(f"\n MARGINAL COSTS (Cost to produce one unit)")
        print("-" * 80)
        while True:
            try:
                self.marginal_cost1 = float(input(f"Enter marginal cost for {self.firm1_name} (e.g., 10): ₹"))
                if self.marginal_cost1 < 0:
                    print(" Cost cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print(" Invalid input. Please enter a number.")
        
        while True:
            try:
                self.marginal_cost2 = float(input(f"Enter marginal cost for {self.firm2_name} (e.g., 10): ₹"))
                if self.marginal_cost2 < 0:
                    print("Cost cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print(" Invalid input. Please enter a number.")
        
        # Market parameters
        print(f"\n MARKET PARAMETERS")
        print("-" * 80)
        print("The demand function is: Price = a - b × Quantity")
        print("Where 'a' is maximum price and 'b' is price sensitivity")
        
        while True:
            try:
                self.price_intercept = float(input("\nEnter 'a' - Maximum market price (e.g., 100): ₹"))
                if self.price_intercept <= max(self.marginal_cost1, self.marginal_cost2):
                    print(f" Maximum price must be greater than marginal costs.")
                    continue
                break
            except ValueError:
                print(" Invalid input. Please enter a number.")
        
        while True:
            try:
                self.price_slope = float(input("Enter 'b' - Price sensitivity (e.g., 1): "))
                if self.price_slope <= 0:
                    print(" Price sensitivity must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                self.market_size = float(input("Enter total market size/demand (e.g., 1000): "))
                if self.market_size <= 0:
                    print(" Market size must be positive.")
                    continue
                break
            except ValueError:
                print(" Invalid input. Please enter a number.")
    
    def calculate_cournot_equilibrium(self):
        """
        Calculate Cournot equilibrium where firms compete on quantity.
        Each firm chooses quantity assuming rival's quantity is fixed.
        """
        print("\n" + "=" * 80)
        print(" " * 20 + "COURNOT MODEL (Quantity Competition)")
        print("=" * 80)
        
        print("\nTHEORY:")
        print("-" * 80)
        print("• Firms choose HOW MUCH to produce simultaneously")
        print("• Market price depends on total quantity: P = a - b(Q1 + Q2)")
        print("• Each firm maximizes profit: Profit = (Price - Cost) x Quantity")
        print("• Equilibrium: Both firms choose best response to each other")
        
        # Cournot best response functions
        # For Firm 1: q1 = (a - c1 - b*q2) / (2b)
        # For Firm 2: q2 = (a - c2 - b*q1) / (2b)
        # Solving simultaneously:
        
        a = self.price_intercept
        b = self.price_slope
        c1 = self.marginal_cost1
        c2 = self.marginal_cost2
        
        # Equilibrium quantities
        q1_star = (a - 2*c1 + c2) / (3*b)
        q2_star = (a - 2*c2 + c1) / (3*b)
        
        # Ensure non-negative quantities
        q1_star = max(0, q1_star)
        q2_star = max(0, q2_star)
        
        # Market price
        total_quantity = q1_star + q2_star
        market_price = a - b * total_quantity
        
        # Profits
        profit1 = (market_price - c1) * q1_star
        profit2 = (market_price - c2) * q2_star
        total_profit = profit1 + profit2
        
        # Revenue
        revenue1 = market_price * q1_star
        revenue2 = market_price * q2_star
        
        print("\n COURNOT EQUILIBRIUM RESULTS:")
        print("-" * 80)
        print(f"\n{self.firm1_name}:")
        print(f"  • Optimal Quantity: {q1_star:.2f} units")
        print(f"  • Revenue: ₹{revenue1:.2f}")
        print(f"  • Total Cost: ₹{c1 * q1_star:.2f}")
        print(f"  • Profit: ₹{profit1:.2f}")
        
        print(f"\n{self.firm2_name}:")
        print(f"  • Optimal Quantity: {q2_star:.2f} units")
        print(f"  • Revenue: ₹{revenue2:.2f}")
        print(f"  • Total Cost: ₹{c2 * q2_star:.2f}")
        print(f"  • Profit: ₹{profit2:.2f}")
        
        print(f"\n MARKET SUMMARY:")
        print(f"  • Market Price: ₹{market_price:.2f}")
        print(f"  • Total Quantity: {total_quantity:.2f} units")
        print(f"  • Total Industry Profit: ₹{total_profit:.2f}")
        print(f"  • {self.firm1_name} Market Share: {(q1_star/total_quantity*100):.1f}%")
        print(f"  • {self.firm2_name} Market Share: {(q2_star/total_quantity*100):.1f}%")
        
        return {
            'q1': q1_star, 'q2': q2_star,
            'price': market_price,
            'profit1': profit1, 'profit2': profit2,
            'revenue1': revenue1, 'revenue2': revenue2,
            'total_quantity': total_quantity
        }
    
    def calculate_bertrand_equilibrium(self):
        
        print("\n" + "=" * 80)
        print(" " * 20 + "BERTRAND MODEL (Price Competition)")
        print("=" * 80)
        
        print("\n THEORY:")
        print("-" * 80)
        print("• Firms choose PRICES simultaneously")
        print("• Consumers buy from the firm with lower price")
        print("• If prices equal, market is split 50-50")
        print("• Result: Intense price competition → 'Race to the bottom'")
        print("• Equilibrium: Both firms price at marginal cost (zero profit!)")
        
        c1 = self.marginal_cost1
        c2 = self.marginal_cost2
        
        equilibrium_price = max(c1, c2)
    
        market_quantity = self.market_size
        
        # If costs are equal, market is split
        if abs(c1 - c2) < 0.01:
            q1 = market_quantity / 2
            q2 = market_quantity / 2
            profit1 = (equilibrium_price - c1) * q1
            profit2 = (equilibrium_price - c2) * q2
        else:
            # Firm with lower cost captures entire market
            if c1 < c2:
                q1 = market_quantity
                q2 = 0
                profit1 = (equilibrium_price - c1) * q1
                profit2 = 0
            else:
                q1 = 0
                q2 = market_quantity
                profit1 = 0
                profit2 = (equilibrium_price - c2) * q2
        
        revenue1 = equilibrium_price * q1
        revenue2 = equilibrium_price * q2
        
        print("\n BERTRAND EQUILIBRIUM RESULTS:")
        print("-" * 80)
        print(f"\n{self.firm1_name}:")
        print(f"  • Equilibrium Price: ₹{equilibrium_price:.2f}")
        print(f"  • Quantity Sold: {q1:.2f} units")
        print(f"  • Revenue: ₹{revenue1:.2f}")
        print(f"  • Total Cost: ₹{c1 * q1:.2f}")
        print(f"  • Profit: ₹{profit1:.2f}")
        
        print(f"\n{self.firm2_name}:")
        print(f"  • Equilibrium Price: ₹{equilibrium_price:.2f}")
        print(f"  • Quantity Sold: {q2:.2f} units")
        print(f"  • Revenue: ₹{revenue2:.2f}")
        print(f"  • Total Cost: ₹{c2 * q2:.2f}")
        print(f"  • Profit: ₹{profit2:.2f}")
        
        print(f"\n MARKET SUMMARY:")
        print(f"  • Market Price: ₹{equilibrium_price:.2f}")
        print(f"  • Total Quantity: {q1 + q2:.2f} units")
        print(f"  • Total Industry Profit: ₹{profit1 + profit2:.2f}")
        
        print("\n  BERTRAND PARADOX:")
        print("With identical products and equal costs, fierce price competition")
        print("drives profits to ZERO! This is why firms try to differentiate products.")
        
        return {
            'price': equilibrium_price,
            'q1': q1, 'q2': q2,
            'profit1': profit1, 'profit2': profit2,
            'revenue1': revenue1, 'revenue2': revenue2
        }
    
    def create_payoff_matrix_example(self):
        """Create and display a simple payoff matrix example"""
        print("\n" + "=" * 80)
        print(" " * 25 + "PAYOFF MATRIX EXAMPLE")
        print("=" * 80)
        
        print("\n CONCEPT:")
        print("-" * 80)
        print("A payoff matrix shows profits for each combination of strategies.")
        print("Example: Price competition with High (₹50) or Low (₹40) pricing")
        
        # Create simple payoff matrix
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.axis('off')
        
        # Define payoffs (Profit1, Profit2)
        payoffs = {
            ('High', 'High'): (5000, 5000),
            ('High', 'Low'): (2000, 7000),
            ('Low', 'High'): (7000, 2000),
            ('Low', 'Low'): (3000, 3000)
        }
        
        # Draw table
        cell_width = 0.25
        cell_height = 0.15
        
        # Headers
        ax.text(0.35, 0.85, self.firm2_name, fontsize=14, fontweight='bold', ha='center')
        ax.text(0.15, 0.65, self.firm1_name, fontsize=14, fontweight='bold', 
                ha='center', rotation=90, va='center')
        
        ax.text(0.35, 0.75, 'High Price', fontsize=12, ha='center', 
                bbox=dict(boxstyle='round', facecolor='lightblue'))
        ax.text(0.6, 0.75, 'Low Price', fontsize=12, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue'))
        
        ax.text(0.15, 0.55, 'High\nPrice', fontsize=11, ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen'))
        ax.text(0.15, 0.35, 'Low\nPrice', fontsize=11, ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen'))
        
        # Payoff cells
        positions = [
            (0.35, 0.55, 'High', 'High'),
            (0.6, 0.55, 'High', 'Low'),
            (0.35, 0.35, 'Low', 'High'),
            (0.6, 0.35, 'Low', 'Low')
        ]
        
        nash_eq = (0.6, 0.35)  # Low, Low is Nash equilibrium
        
        for x, y, s1, s2 in positions:
            p1, p2 = payoffs[(s1, s2)]
            
            # Highlight Nash equilibrium
            if (x, y) == nash_eq:
                rect = Rectangle((x-0.1, y-0.07), 0.2, 0.14, 
                                linewidth=3, edgecolor='red', 
                                facecolor='yellow', alpha=0.3)
                ax.add_patch(rect)
                ax.text(x, y+0.09, ' NASH EQUILIBRIUM', fontsize=9, 
                       ha='center', color='red', fontweight='bold')
            
            ax.text(x, y+0.02, f'₹{p1:,}', fontsize=11, ha='center', 
                   color='darkgreen', fontweight='bold')
            ax.text(x, y-0.02, f'₹{p2:,}', fontsize=11, ha='center',
                   color='darkblue', fontweight='bold')
        
        # Legend
        ax.text(0.47, 0.15, f'Green = {self.firm1_name} profit', 
               fontsize=10, color='darkgreen', fontweight='bold')
        ax.text(0.47, 0.11, f'Blue = {self.firm2_name} profit', 
               fontsize=10, color='darkblue', fontweight='bold')
        
        ax.text(0.47, 0.05, 'Nash Equilibrium: Both firms choose Low Price',
               fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        plt.title('Payoff Matrix: Price Competition Game', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.show()
        
        print("\n INTERPRETATION:")
        print("-" * 80)
        print("• If both choose High: Both get ₹5,000 (cooperation)")
        print("• If one goes Low: That firm gets ₹7,000, other gets ₹2,000")
        print("• If both choose Low: Both get ₹3,000 (Nash equilibrium)")
        print("\n Nash Equilibrium = Both choose LOW PRICE")
        print("   Neither firm can improve by unilaterally changing strategy!")
    
    def plot_cournot_visualizations(self, cournot_results):
        
        a = self.price_intercept
        b = self.price_slope
        c1 = self.marginal_cost1
        c2 = self.marginal_cost2
        q1_star = cournot_results['q1']
        q2_star = cournot_results['q2']
        
        fig = plt.figure(figsize=(18, 12))
        
        # 1. Reaction Functions (Best Response Curves)
        ax1 = plt.subplot(2, 3, 1)
        q2_range = np.linspace(0, (a - c1)/b, 100)
        q1_range = np.linspace(0, (a - c2)/b, 100)
        
        # Firm 1's reaction function: q1 = (a - c1 - b*q2) / (2b)
        r1 = (a - c1 - b*q2_range) / (2*b)
        r1 = np.maximum(r1, 0)
        
        # Firm 2's reaction function: q2 = (a - c2 - b*q1) / (2b)
        r2 = (a - c2 - b*q1_range) / (2*b)
        r2 = np.maximum(r2, 0)
        
        ax1.plot(q2_range, r1, 'b-', linewidth=2, label=f'{self.firm1_name} Reaction')
        ax1.plot(r2, q1_range, 'r-', linewidth=2, label=f'{self.firm2_name} Reaction')
        ax1.plot(q2_star, q1_star, 'go', markersize=15, label='Cournot Equilibrium')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlabel(f'{self.firm2_name} Quantity', fontsize=11)
        ax1.set_ylabel(f'{self.firm1_name} Quantity', fontsize=11)
        ax1.set_title('Reaction Functions\n(Best Response Curves)', fontsize=12, fontweight='bold')
        ax1.legend()
        
        # 2. Market Share Pie Chart
        ax2 = plt.subplot(2, 3, 2)
        sizes = [q1_star, q2_star]
        colors = ['pink', 'green']
        explode = (0.05, 0.05)
        ax2.pie(sizes, explode=explode, labels=[self.firm1_name, self.firm2_name],
                colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        ax2.set_title('Market Share\n(Quantity)', fontsize=12, fontweight='bold')
        
        # 3. Profit Comparison Bar Chart
        ax3 = plt.subplot(2, 3, 3)
        firms = [self.firm1_name, self.firm2_name]
        profits = [cournot_results['profit1'], cournot_results['profit2']]
        bars = ax3.bar(firms, profits, color=['pink', 'green'], edgecolor='black', linewidth=2)
        ax3.set_ylabel('Profit (₹)', fontsize=11)
        ax3.set_title('Profit Comparison', fontsize=12, fontweight='bold')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'₹{height:.0f}', ha='center', va='bottom', fontweight='bold')
        
        # 4. 3D Profit Surface for Firm 1
        ax4 = plt.subplot(2, 3, 4, projection='3d')
        q1_grid = np.linspace(0, (a-c1)/(2*b), 30)
        q2_grid = np.linspace(0, (a-c2)/(2*b), 30)
        Q1, Q2 = np.meshgrid(q1_grid, q2_grid)
        
        # Profit for Firm 1: π1 = (P - c1)*q1 where P = a - b(q1+q2)
        P_grid = a - b*(Q1 + Q2)
        Profit1_grid = (P_grid - c1) * Q1
        Profit1_grid = np.maximum(Profit1_grid, 0)
        
        surf = ax4.plot_surface(Q1, Q2, Profit1_grid, cmap='viridis', alpha=0.8)
        ax4.scatter([q1_star], [q2_star], [cournot_results['profit1']], 
                   color='red', s=100, label='Equilibrium')
        ax4.set_xlabel(f'{self.firm1_name} Qty', fontsize=9)
        ax4.set_ylabel(f'{self.firm2_name} Qty', fontsize=9)
        ax4.set_zlabel('Profit (₹)', fontsize=9)
        ax4.set_title(f'{self.firm1_name} Profit Surface', fontsize=11, fontweight='bold')
        
        # 5. Revenue vs Cost Breakdown
        ax5 = plt.subplot(2, 3, 5)
        categories = [f'{self.firm1_name}', f'{self.firm2_name}']
        revenue = [cournot_results['revenue1'], cournot_results['revenue2']]
        costs = [c1 * q1_star, c2 * q2_star]
        
        x = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax5.bar(x - width/2, revenue, width, label='Revenue', color='lightgreen', edgecolor='black')
        bars2 = ax5.bar(x + width/2, costs, width, label='Total Cost', color='lightcoral', edgecolor='black')
        
        ax5.set_ylabel('Amount (₹)', fontsize=11)
        ax5.set_title('Revenue vs Cost Analysis', fontsize=12, fontweight='bold')
        ax5.set_xticks(x)
        ax5.set_xticklabels(categories)
        ax5.legend()
        ax5.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax5.text(bar.get_x() + bar.get_width()/2., height,
                        f'₹{height:.0f}', ha='center', va='bottom', fontsize=9)
        
        # 6. Demand Curve and Market Equilibrium
        ax6 = plt.subplot(2, 3, 6)
        Q_range = np.linspace(0, a/b, 100)
        P_range = a - b*Q_range
        
        ax6.plot(Q_range, P_range, 'b-', linewidth=2, label='Demand Curve')
        ax6.axhline(y=cournot_results['price'], color='r', linestyle='--', 
                   linewidth=2, label=f"Equilibrium Price (₹{cournot_results['price']:.2f})")
        ax6.axvline(x=cournot_results['total_quantity'], color='g', linestyle='--',
                   linewidth=2, label=f"Total Quantity ({cournot_results['total_quantity']:.2f})")
        ax6.plot(cournot_results['total_quantity'], cournot_results['price'], 
                'ro', markersize=12, label='Market Equilibrium')
        
        ax6.set_xlabel('Total Quantity', fontsize=11)
        ax6.set_ylabel('Price (₹)', fontsize=11)
        ax6.set_title('Market Demand & Equilibrium', fontsize=12, fontweight='bold')
        ax6.legend()
        ax6.grid(True, alpha=0.3)
        
        plt.suptitle(f'COURNOT MODEL ANALYSIS: {self.firm1_name} vs {self.firm2_name}',
                    fontsize=16, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.show()
    
    def plot_bertrand_visualizations(self, bertrand_results):
        
        fig = plt.figure(figsize=(16, 10))
        
        # 1. Price Competition Game Tree
        ax1 = plt.subplot(2, 3, 1)
        ax1.axis('off')
        ax1.text(0.5, 0.9, 'BERTRAND PRICE COMPETITION', 
                ha='center', fontsize=13, fontweight='bold')
        
        # Simple representation
        price_scenarios = ['Both High\n(₹50)', 'Mixed\nPricing', 'Both at Cost\n(Equilibrium)']
        outcomes = ['Moderate\nProfits', 'Winner takes\nall', 'Zero\nProfit']
        
        for i, (scenario, outcome) in enumerate(zip(price_scenarios, outcomes)):
            y_pos = 0.7 - i*0.25
            ax1.text(0.2, y_pos, scenario, ha='center', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor='lightblue'))
            ax1.arrow(0.3, y_pos, 0.15, 0, head_width=0.03, head_length=0.02, fc='black')
            
            color = 'lightcoral' if i == 2 else 'lightgreen'
            ax1.text(0.55, y_pos, outcome, ha='center', fontsize=10,
                    bbox=dict(boxstyle='round', facecolor=color))
        
        ax1.text(0.5, 0.05, ' Race to the Bottom: Prices → Marginal Cost',
                ha='center', fontsize=11, fontweight='bold', color='red')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        
        # 2. Quantity Distribution
        ax2 = plt.subplot(2, 3, 2)
        firms = [self.firm1_name, self.firm2_name]
        quantities = [bertrand_results['q1'], bertrand_results['q2']]
        colors = ['pink', 'blue']
        
        bars = ax2.bar(firms, quantities, color=colors, edgecolor='black', linewidth=2)
        ax2.set_ylabel('Quantity Sold', fontsize=11)
        ax2.set_title('Quantity Distribution', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
        
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.0f} units', ha='center', va='bottom', fontweight='bold')
        
        # 3. Profit Comparison
        ax3 = plt.subplot(2, 3, 3)
        profits = [bertrand_results['profit1'], bertrand_results['profit2']]
        bars = ax3.bar(firms, profits, color=colors, edgecolor='black', linewidth=2)
        ax3.set_ylabel('Profit (₹)', fontsize=11)
        ax3.set_title('Profit Comparison\n(Zero or Near-Zero!)', fontsize=12, fontweight='bold')
        ax3.grid(True, alpha=0.3, axis='y')
        
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'₹{height:.0f}', ha='center', va='bottom', fontweight='bold')
        
        # 4. Revenue vs Cost
        ax4 = plt.subplot(2, 3, 4)
        categories = [self.firm1_name, self.firm2_name]
        revenue = [bertrand_results['revenue1'], bertrand_results['revenue2']]
        costs = [self.marginal_cost1 * bertrand_results['q1'], 
                 self.marginal_cost2 * bertrand_results['q2']]
        
        x = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax4.bar(x - width/2, revenue, width, label='Revenue', 
                       color='lightgreen', edgecolor='black')
        bars2 = ax4.bar(x + width/2, costs, width, label='Total Cost', 
                       color='lightcoral', edgecolor='black')
        
        ax4.set_ylabel('Amount (₹)', fontsize=11)
        ax4.set_title('Revenue vs Cost Analysis', fontsize=12, fontweight='bold')
        ax4.set_xticks(x)
        ax4.set_xticklabels(categories)
        ax4.legend()
        ax4.grid(True, alpha=0.3, axis='y')
        
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax4.text(bar.get_x() + bar.get_width()/2., height,
                        f'₹{height:.0f}', ha='center', va='bottom', fontsize=9)
        
        # 5. Price Comparison Timeline
        ax5 = plt.subplot(2, 3, 5)
        
        # Simulate price war progression
        iterations = ['Start', 'Round 1', 'Round 2', 'Round 3', 'Equilibrium']
        firm1_prices = [self.price_intercept * 0.8, 
                       self.price_intercept * 0.6,
                       self.price_intercept * 0.4,
                       max(self.marginal_cost1, self.marginal_cost2) * 1.1,
                       bertrand_results['price']]
        firm2_prices = [self.price_intercept * 0.85,
                       self.price_intercept * 0.55,
                       self.price_intercept * 0.38,
                       max(self.marginal_cost1, self.marginal_cost2) * 1.05,
                       bertrand_results['price']]
        
        x_pos = np.arange(len(iterations))
        ax5.plot(x_pos, firm1_prices, 'o-', linewidth=2, markersize=8, 
                label=self.firm1_name, color='pink')
        ax5.plot(x_pos, firm2_prices, 's-', linewidth=2, markersize=8,
                label=self.firm2_name, color='blue')
        ax5.axhline(y=max(self.marginal_cost1, self.marginal_cost2), 
                   color='red', linestyle='--', linewidth=2, 
                   label='Marginal Cost Floor')
        
        ax5.set_xticks(x_pos)
        ax5.set_xticklabels(iterations, rotation=45)
        ax5.set_ylabel('Price (₹)', fontsize=11)
        ax5.set_title('Price War Progression\n(Race to Bottom)', fontsize=12, fontweight='bold')
        ax5.legend()
        ax5.grid(True, alpha=0.3)
        
        # 6. Market Share Pie Chart
        ax6 = plt.subplot(2, 3, 6)
        if bertrand_results['q1'] > 0 or bertrand_results['q2'] > 0:
            sizes = [bertrand_results['q1'], bertrand_results['q2']]
            colors_pie = ['pink', 'blue']
            explode = (0.05, 0.05)
            ax6.pie(sizes, explode=explode, labels=[self.firm1_name, self.firm2_name],
                   colors=colors_pie, autopct='%1.1f%%', shadow=True, startangle=90)
            ax6.set_title('Market Share\n(Quantity)', fontsize=12, fontweight='bold')
        else:
            ax6.text(0.5, 0.5, 'No Sales\n(Prices too high)', 
                    ha='center', va='center', fontsize=14, fontweight='bold')
            ax6.set_xlim(0, 1)
            ax6.set_ylim(0, 1)
            ax6.axis('off')
        
        plt.suptitle(f'BERTRAND MODEL ANALYSIS: {self.firm1_name} vs {self.firm2_name}',
                    fontsize=16, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.show()
    
    def compare_models(self, cournot_results, bertrand_results):
        
        print("\n" + "=" * 80)
        print(" " * 20 + "COURNOT vs BERTRAND COMPARISON")
        print("=" * 80)
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Profit Comparison
        ax1 = axes[0, 0]
        models = ['Cournot\n(Quantity)', 'Bertrand\n(Price)']
        firm1_profits = [cournot_results['profit1'], bertrand_results['profit1']]
        firm2_profits = [cournot_results['profit2'], bertrand_results['profit2']]
        
        x = np.arange(len(models))
        width = 0.35
        
        bars1 = ax1.bar(x - width/2, firm1_profits, width, label=self.firm1_name,
                       color='pink', edgecolor='black')
        bars2 = ax1.bar(x + width/2, firm2_profits, width, label=self.firm2_name,
                       color='blue', edgecolor='black')
        
        ax1.set_ylabel('Profit (₹)', fontsize=11)
        ax1.set_title('Profit Comparison Across Models', fontsize=12, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(models)
        ax1.legend()
        ax1.grid(True, alpha=0.3, axis='y')
        
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height,
                        f'₹{height:.0f}', ha='center', va='bottom', fontsize=9)
        
        # 2. Quantity Comparison
        ax2 = axes[0, 1]
        firm1_qty = [cournot_results['q1'], bertrand_results['q1']]
        firm2_qty = [cournot_results['q2'], bertrand_results['q2']]
        
        bars1 = ax2.bar(x - width/2, firm1_qty, width, label=self.firm1_name,
                       color='pink', edgecolor='black')
        bars2 = ax2.bar(x + width/2, firm2_qty, width, label=self.firm2_name,
                       color='green', edgecolor='black')
        
        ax2.set_ylabel('Quantity', fontsize=11)
        ax2.set_title('Quantity Comparison Across Models', fontsize=12, fontweight='bold')
        ax2.set_xticks(x)
        ax2.set_xticklabels(models)
        ax2.legend()
        ax2.grid(True, alpha=0.3, axis='y')
        
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.1f}', ha='center', va='bottom', fontsize=9)
        
        # 3. Price Comparison
        ax3 = axes[1, 0]
        prices = [cournot_results['price'], bertrand_results['price']]
        bars = ax3.bar(models, prices, color=['green', 'blue'], edgecolor='black', linewidth=2)
        ax3.set_ylabel('Market Price (₹)', fontsize=11)
        ax3.set_title('Price Comparison Across Models', fontsize=12, fontweight='bold')
        ax3.grid(True, alpha=0.3, axis='y')
        
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'₹{height:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        # 4. Key Insights Table
        ax4 = axes[1, 1]
        ax4.axis('off')
        
        table_data = [
            ['Metric', 'Cournot', 'Bertrand'],
            ['Competition On', 'Quantity', 'Price'],
            ['Market Price', f'₹{cournot_results["price"]:.2f}', f'₹{bertrand_results["price"]:.2f}'],
            ['Total Profit', f'₹{cournot_results["profit1"]+cournot_results["profit2"]:.0f}', 
             f'₹{bertrand_results["profit1"]+bertrand_results["profit2"]:.0f}'],
            ['Winner', 'Both share market', 'Lower cost firm' if self.marginal_cost1 != self.marginal_cost2 else 'Split market'],
            ['Profit Level', 'Moderate', 'Zero/Very Low']
        ]
        
        table = ax4.table(cellText=table_data, cellLoc='center', loc='center',
                         colWidths=[0.3, 0.35, 0.35])
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2.5)
        
        # Style header row
        for i in range(3):
            table[(0, i)].set_facecolor('blue')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # Alternate row colors
        for i in range(1, len(table_data)):
            for j in range(3):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor('white')
        
        ax4.set_title('Key Insights Comparison', fontsize=12, fontweight='bold', pad=20)
        
        plt.suptitle(f'MODEL COMPARISON: {self.firm1_name} vs {self.firm2_name}',
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        # Print summary
        print("\n KEY TAKEAWAYS:")
        print("-" * 80)
        print(f"1. COURNOT MODEL (Quantity Competition):")
        print(f"   • Both firms produce and share market")
        print(f"   • Moderate profits: ₹{cournot_results['profit1']+cournot_results['profit2']:.0f}")
        print(f"   • Higher prices: ₹{cournot_results['price']:.2f}")
        
        print(f"\n2. BERTRAND MODEL (Price Competition):")
        print(f"   • Fierce price competition")
        print(f"   • Low/Zero profits: ₹{bertrand_results['profit1']+bertrand_results['profit2']:.0f}")
        print(f"   • Prices drop to cost: ₹{bertrand_results['price']:.2f}")
        
        print(f"\n3. REAL-WORLD IMPLICATIONS:")
        print(f"   • Pure price competition (Bertrand) is devastating for profits")
        print(f"   • Firms prefer product differentiation to escape price wars")
        print(f"   • Quantity competition (Cournot) allows for better profitability")
        print(f"   • This explains why companies invest heavily in branding!")
    
    def run_simulation(self):
    
        self.display_introduction()
        self.get_user_inputs()
        
        print("\n" + " CALCULATING COURNOT EQUILIBRIUM..." + "\n")
        cournot_results = self.calculate_cournot_equilibrium()
        
        input("\nPress Enter to view Cournot visualizations...")
        self.plot_cournot_visualizations(cournot_results)
        
        print("\n" + " CALCULATING BERTRAND EQUILIBRIUM..." + "\n")
        bertrand_results = self.calculate_bertrand_equilibrium()
        
        input("\nPress Enter to view Bertrand visualizations...")
        self.plot_bertrand_visualizations(bertrand_results)
        
        input("\nPress Enter to view Payoff Matrix example...")
        self.create_payoff_matrix_example()
        
        input("\nPress Enter to view model comparison...")
        self.compare_models(cournot_results, bertrand_results)
        
        # Final summary
        print("\n" + "=" * 80)
        print(" " * 25 + "SIMULATION COMPLETE!")
        print("=" * 80)
        print("\n You have explored:")
        print("   • Duopoly fundamentals and real-world examples")
        print("   • Cournot Model (quantity competition)")
        print("   • Bertrand Model (price competition)")
        print("   • Payoff matrices and Nash equilibrium")
        print("   • Comprehensive visualizations and comparisons")
        print("\n Key Insight: Game theory helps firms make optimal strategic decisions")
        print("   when outcomes depend on competitors' actions!")
        print("=" * 80)

# main execution
print("\n" + "=" * 80)
print("WELCOME TO DUOPOLY GAME THEORY SIMULATOR".center(80))
print("=" * 80)
print("\nThis program demonstrates strategic competition between two firms")
print("using Cournot and Bertrand models from Game Theory.")
print("=" * 80 + "\n")
    
game = DuopolyGame()
game.run_simulation()
    
print("\n" + "=" * 80)
print("Thank you for using the Duopoly Game Theory Simulator!")
print("=" * 80)